from app import create_app


app, socketio_app = create_app()
socketio_app.run(
    app,
    host=app.config.get('HOST'),
    port=app.config.get('PORT')
)
