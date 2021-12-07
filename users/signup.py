from django.contrib import messages

def signup(request):
    # redirect a user to the home page if he is already logged in
    if request.user.is_authenticated:
        return redirect('blog:home')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Congratulations, you are now a registered user!")
            return redirect('blog:home')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})