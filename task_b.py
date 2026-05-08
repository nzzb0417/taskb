slug = input("Enter the title that you want to turn into a slug: ")

slug = slug.lower()
slug = slug.replace(" a ", " ")
slug = slug.replace(" the ", " ")
slug = slug.replace("a ", "")
slug = slug.replace("the ", "")
slug = slug.strip()
slug = slug.replace(" ", "-")

print(f"slug = {slug[0:25]}")
