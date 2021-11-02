from django.http.request import HttpRequest
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from .models import Ingridient, Recipe
from .forms import filter_ingridient, search_recipe, RegistrationForm, LoginForm, CreateRecipe, CreateIngridient
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout

def index(request):
    ingridients = Ingridient.objects.all().order_by('title')
    filter = filter_ingridient()
    search = search_recipe()
    if request.method == 'POST':
        try:
            recipes = Ingridient.objects.get(id=int(request.POST['value'])).recipes.all()
        except:
            recipes_tmp = Recipe.objects.all().order_by('publish_date')
            recipes = []
            for recipe in recipes_tmp:
                if (recipe.title.find(request.POST['value']) != -1) or (recipe.title.upper().find(request.POST['value']) != -1) or (recipe.title.lower().find(request.POST['value']) != -1):
                    recipes.append(Recipe.objects.get(id=recipe.pk))
                
    else:
        recipes = Recipe.objects.all().order_by('publish_date')
    return render(request, 'book/main_page.html', {'recipes': recipes, 'ingridients': ingridients, 'form': filter, 'search': search})


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'book/recipe.html', {'recipe': recipe})


def registration(request):
    if request.method == 'POST':
        check_register = RegistrationForm(request.POST)
        if check_register.is_valid():
            new_user = check_register.save(commit=False)
            new_user.set_password(check_register.cleaned_data['password'])
            new_user.last_login = timezone.now()
            new_user.save()
            return render(request, 'book/registr_done.html', {"new_user": new_user})
        else:
            print(check_register.is_valid())
            return HttpResponse("USER ARE EXIST")
    else:
        register_form = RegistrationForm()
        return render(request, 'book/register.html', {"register_form": register_form})


def loginview(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
                else:
                    return HttpResponse('Disable account')
            else:
                return HttpResponse('Invalid login')
        else:
            return HttpResponse('Invalid data')
    else:
        form = LoginForm()
        return render(request, 'book/autorize.html', {'form': form})


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect(index)


def create_ingridient(request):
    if request.method == 'POST':
        new_ingridient = CreateIngridient(request.POST)
        if new_ingridient.is_valid:
            if len(Ingridient.objects.filter(title__lte=request.POST['title'])) ==  0:
                new_ingridient.save()
    form = CreateIngridient()
    return render(request, 'book/create_ingridient.html', {'form': form})


def create_recipe(request):
    if request.method == 'POST':
        new_recipe = CreateRecipe(request.POST)
        if new_recipe.is_valid:
            recipe = new_recipe.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('recipe_detail', pk=recipe.pk)
    form = CreateRecipe()
    return render(request, 'book/create_recipe.html', {'form': form})

