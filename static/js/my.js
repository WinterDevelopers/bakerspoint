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

const paymentForm = document.getElementById('payment-button');

    paymentForm.addEventListener('click', function payWithPaystack(e){

        e.preventDefault();

        let handler = PaystackPop.setup({
        
            key: 'pk_test_23927c5cef5c5185b7c8faa79ce9191ad90a4f31', // Replace with your public key

            email: document.getElementById('email').textContent,
            
            amount: document.getElementById('amout').textContent*100,

            ref: ''+Math.floor((Math.random() * 1000000000) + 1), // generates a pseudo-unique reference. Please replace with a reference you generated. Or remove the line entirely so our API will generate one for you

            // label: "Optional string that replaces customer email"

            onClose: function(){
                
                alert('paystack payment pop up was closed closed.');

            },

            callback: function(response){

            let message = 'Payment complete! Reference: ' + response.reference + ' please make sure you save this or screenshot it.. thank you';

            alert(message);
           

            tracking = response.reference
            
            fetch('/notification/',{
                method:'POST',
                headers:{
                    'Content-Type':'application/json',
                    'X-CSRFToken':csrftoken,
                },
                body:JSON.stringify({'tracking':tracking}),
            } )

                .then((response)=> {
                    return response.json()
                })

                .then((data) => {
                    console.log('saved to customer notification', data)
                })
            
            submitFormData();
            }

        });

        handler.openIframe();

    } );

 