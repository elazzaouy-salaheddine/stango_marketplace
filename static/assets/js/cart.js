var updateBtns = document.getElementsByClassName('update-cart')


for (i=0; i< updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product 
        var action = this.dataset.action
        console.log('productId:', productId, 'Action:', action)

        console.log('USER', user)
        if (user=='AnonymousUser') {
            console.log(user);
        }
        else{
            updateUserOrder(productId, action)
        }
    })
}


function updateUserOrder(productId, action){
    console.log('user logged in send data')
    var url = '/order/updateitem/'
    fetch(url, {
        method:'POST',
        headers:{
            'Content-type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({
            'productId':productId,'action': action
        }) 
    })
    .then((res)=>{
        return res.json()
    })
    .then((data)=>{
        location.reload()
    })
}