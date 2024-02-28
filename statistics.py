def statistics():
    path_file = input("enter the path of the text file ")
    with open(path_file, "r") as file:
        content = file.read()

        words = content.split(" ")
        print(f"the number of words is: {len(words)}")
        unique = set(words)
        print(f"Number of unique words: {len(unique)}")

        word_counts = {}
        for word in words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1

        for word, count in word_counts.items():
            print(f"{word},{count}")


statistics()
