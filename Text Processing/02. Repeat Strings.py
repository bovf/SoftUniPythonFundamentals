words = input().split()
end_result = ""

for word in words:
    end_result += word * len(word)

print(end_result)
