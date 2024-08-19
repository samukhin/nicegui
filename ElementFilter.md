https://nicegui.io/documentation/element_filter


```py

for element in ElementFilter():
    if "label" in str(type(element)):
        print(element)
        element.delete()

```
