from exchange import Exchange

if __name__ == '__main__':
    app = Exchange()
    app.run("127.0.0.1", 8888)
    
 
   
"""
app = Exchange()

router = app.Router()

router.post("/login", loginRouter)
router.get("/Submit", submitRouter)
app.use(router)

app.staticDir(__name__)

app.use(CSRFMiddle, "middleware")


app.run("127.0.0.1", 8888)

"""