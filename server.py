from aiohttp import web


def run_daylighting_simulation(lat, lng):
    return 'Latitude is %s and longitude is %s' % (lat, lng)


async def handle(request):
    lng = request.match_info.get('lng', '-33.600')
    lat = request.match_info.get('lat', '123.600')
    res = run_daylighting_simulation(lat, lng)
    return web.Response(text=res)


def run():
    app = web.Application()
    app.add_routes(
        [
            web.get('/', handle),
            web.get('/{lat}/{lng}', handle)
        ]
    )
    web.run_app(app)


if __name__ == '__main__':
    run()
