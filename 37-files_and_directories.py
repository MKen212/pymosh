from pathlib import Path

path1 = Path("ecommerce")
print(path1.exists())

path2 = Path("emails")
print(path2.exists())
print(path2.mkdir())
print(path2.exists())
print(path2.rmdir())
print(path2.exists())

path3 = Path()
for file in path3.glob("*"):
    print(file)
