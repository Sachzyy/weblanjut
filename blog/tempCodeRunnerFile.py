@api_view(['GET'])
def artikel_list (request, x_api_key):
    key = 'fadil'
    if key != 'x_api_key':
        content = {
            'status': False,
            'message': 'Invalid Key'
        }
        return Response (content)
    list = Artikel.objects.all()
    jumlah_artikel = list.count()
    serializer = ArtikelSerializer(list, many=True)
    content = {
        'status': True,
        'records' : jumlah_artikel,
        'rows' : serializer.data

    }
    return Response(content)