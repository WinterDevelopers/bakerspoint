console.log('winter developers')

var updateBtns = document.getElementsByClassName('update-cart')


for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:',productId, 'action:',action)

        console.log('User:',user)

        if(user == 'AnonymousUser'){
            console.log('user not logged in')
            if(action=='add'){
                if(cart[productId] == undefined){
                    cart[productId] = {'quantity':1}
                    console.log(cart[productId])
                }
                else{
                    cart[productId]['quantity'] +=1
                }
            }
            if(action == 'remove'){
                cart[productId]['quantity'] -=1

                if(cart[productId]['quantity'] <= 0){
                    delete cart[productId]
                    console.log('item was deleted')
                }
            }
            console.log('cart:', cart)
            document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=; path=/";
            location.reload()
        }

        else{
            updateUserItem(productId, action)
        }
    })
}

function updateUserItem(productId, action){
    console.log('user logged in sending data....')
    var url = '/update-item/'

    fetch(url, {
        method : 'POST',
        headers : {
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'productId':productId, 'action':action }),
    })

        .then((response) => {
            return response.json()
        })

        .then((data) => {
            console.log('data',data)
            location.reload()
        });
}



 