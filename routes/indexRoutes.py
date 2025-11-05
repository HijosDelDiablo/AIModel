from fastapi import FastAPI

class IndexRoutes:
    def __init__(self, app: FastAPI, routes: list):
        self.app = app
        self.routes = routes
        self.register_routes()

    def register_routes(self):
        for route in self.routes:
            self.app.include_router(route.router)
        return self.app