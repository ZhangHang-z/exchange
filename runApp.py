from exchange import make_app, Exchange

if __name__ == '__main__':
    make_app()
    
 
   
"""
app = Exchange()

get_router = {
    ("/user", userRouter),
    ("/home", homePouter)
}

post_router = {
    ("/login", loginRouter),
    ("/Submit", submitRouter)
}

app.staticDir(__name__)
app.use(CSRFMiddle, "middleware")
app.use(get_router, "GET")
app.use(post_router, "POST")
"""