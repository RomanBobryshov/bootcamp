def new_note(note_len_dict, rating_dict):
    author_name = input("enter the author's name:")
    note = input("enter the note:")
    note_len_dict[author_name] = len(note)
    rating = float(input('enter the rating (from 0 to 1):'))
    if rating < 0 or rating > 1:
        print('Specify a rating in the range 0 to 1')
        new_note(note_len_dict, rating_dict)
    else:
        rating_dict[author_name] = rating
        return edd_note_to_file(author_name, note, rating)


def edd_note_to_file(author_name, note, rating):
    with open('microlib.txt', 'a', encoding='UTF-8')as f:
        f.write('author_name {}\nnote {}\nrating {}\n'.format(author_name, note, rating))


def read_notes_from_file(note_len_dict, author_name=None):
    with open('microlib.txt', 'r', encoding='UTF-8')as f:
        text = f.read()
        if author_name is None:
            print(text)
        else:
            index = text.find("{}".format(author_name))
            f.seek(index+len(author_name)+len('note   '))
            print(f.read(note_len_dict.get(author_name)))


def author_with_the_highest_rating(rating_dict):
    rating_list = list(rating_dict.items())
    rating_list.sort(key=lambda i: i[1])
    highest_rating = rating_list[-1:]
    for i in highest_rating:
        print(i[0], ':', i[1])


def author_with_the_lowest_rating(rating_dict):
    rating_list = list(rating_dict.items())
    print(rating_list.sort(key=lambda i: i[1]))
    lowest_rating = rating_list[:1]
    for i in lowest_rating:
        print(i[0], ':', i[1])


def average_rating_among_all_authors(rating_dict):
    rating_list = list(rating_dict.items())
    new_rating_list = []
    for i in rating_list:
        new_rating_list.append(i[1])
    print(sum(new_rating_list) / len(new_rating_list))


def event_loop():
    note_len_dict = {}
    rating_dict = {}
    while True:
        input_space = input('Select one of the suggested options:Add new note/Read notes from file/\n'
                            'Get author with the highest rating/Get author with the lowest rating/\n'
                            'Get average rating among all authors:')
        if input_space is None:
            event_loop()
        elif input_space =='Add new note':
            new_note(note_len_dict, rating_dict)
        elif input_space =='Read notes from file':
            name_input = input("enter the author's name:")
            read_notes_from_file(note_len_dict, author_name=name_input)
        elif input_space =='Get author with the highest rating':
            author_with_the_highest_rating(rating_dict)
        elif input_space =='Get author with the lowest rating':
            author_with_the_lowest_rating(rating_dict)
        elif input_space =='Get average rating among all authors':
            average_rating_among_all_authors(rating_dict)


if __name__ == '__main__':
    event_loop()
