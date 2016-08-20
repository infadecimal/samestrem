from flask import jsonify, request
from app import app


@app.errorhandler(403)
def permission_denied(e):
    app.logger.error('ERROR 403: Permission Denied')
    response = jsonify(
        success=False,
        message="You do not have permission so access this endpoint"
    )
    response.status_code = 403
    return response


@app.errorhandler(404)
def page_not_found(e):
    app.logger.error('ERROR 404: Page Not Found: %s', (request.path))
    response = jsonify(
        success=False,
        message="That endpoint was not found"
    )
    response.status_code = 404
    return response
