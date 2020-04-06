from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'wordcount/home.html')
def about(request):
    return render(request, 'wordcount/about.html')
def result(request):
    text = request.GET['fulltext']
    words = text.split()

    word_dict = {}
    for x in words:
        if x in word_dict:
            word_dict[x] += 1
        else:
            word_dict[x] = 1

    return render(request, 'wordcount/result.html', {'total': text, 'dict':word_dict.items()})
