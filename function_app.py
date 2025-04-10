import azure.functions as func
import logging

app = func.FunctionApp()

@app.function_name(name="PingFunction")
@app.route(route="ping", auth_level=func.AuthLevel.ANONYMOUS)
def ping(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Ping endpoint was hit.")
    return func.HttpResponse("pong", status_code=200)
