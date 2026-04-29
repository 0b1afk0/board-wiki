from django.shortcuts import render, get_object_or_404, redirect
from .models import Game, Comment, Tag

def g_list(request):
    games = Game.objects.prefetch_related('tags').all()
    tags = Tag.objects.all()
    
    return render(request, 'g/list.html', {'games': games, 'tags': tags})


def g_detail(request, game_id):
    game = get_object_or_404(Game, id=game_id)

    if request.POST.get("website"):
        return redirect('g_detail', game_id=game.id)

    if request.method == "POST":
        author = request.POST.get("author", "").strip()
        text = request.POST.get("text", "").strip()
        errors = []

        # Валидация имени автора
        if not author:
            errors.append("Введите ваше имя")
        elif len(author) < 2:
            errors.append("Имя должно быть не менее 2 символов")
        elif len(author) > 30:
            errors.append("Имя должно быть не более 30 символов")
        # Проверка на повторяющиеся символы
        elif all(c == author[0] for c in author):
            errors.append("Введите нормальное имя")
        # Проверка что есть хотя бы одна буква
        elif not any(c.isalpha() for c in author):
            errors.append("Имя должно содержать буквы")

        # Валидация текста комментария
        if not text:
            errors.append("Введите текст комментария")
        elif len(text) < 5:
            errors.append("Комментарий должен быть не менее 5 символов")
        elif len(text) > 90:
            errors.append("Комментарий должен быть не более 90 символов")
        elif all(c == text[0] for c in text):
            errors.append("Введите нормальный комментарий")

        if not errors:
            Comment.objects.create(
                game=game,
                author=author,
                text=text
            )
            return redirect('g_detail', game_id=game.id)
        else:
            # Если есть ошибки, передаем их в шаблон
            return render(request, 'g/detail.html', {
                'game': game,
                'errors': errors,
                'old_author': author,
                'old_text': text
            })

    return render(request, 'g/detail.html', {'game': game})


def page_not_found(request, exception=None):
    return render(request, '404.html', status=404)
