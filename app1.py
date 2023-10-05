import openai


def crear_imagen(descripcion):
    openai.api_key = "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"
    openai.Model.list()
    respuesta = openai.Image.create(
        prompt=descripcion,
        n=1,
        size="512x512"
    )
    return respuesta["data"][0]["url"]
    #return respuesta["data"]


if __name__ == "__main__":
    descripcion = input("Ingresa la descripcion de la imagen a generar: ")
    res = crear_imagen(descripcion)
    print(res)
    #for url in res:
    #    print(url["url"])