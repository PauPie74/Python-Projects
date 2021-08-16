import wikipedia

result = wikipedia.page("Enigmarelle")
print(result.summary)

#print(result.content)

print(result.categories)

#print(result.html())

print(result.images)

print(result.links)

#Random articles' titles
print(wikipedia.random(pages=5))

print(result.references)

print(wikipedia.search('dog', results=10, suggestion=False))

print(result.section('Presentation'))

print(wikipedia.summary('Enigmarelle', sentences = 2))
