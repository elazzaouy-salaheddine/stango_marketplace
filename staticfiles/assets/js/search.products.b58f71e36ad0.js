const searchfield = document.getElementById('search');


searchfield.addEventListener('keyup',(e) =>{
    const searchValue = e.target.value;
    if (searchValue.length >0 ) {
        
        fetch('/products/serach-products/',{
            body: JSON.stringify({searche:searchValue}),
            method:'POST',
        })
        .then((res)=> res.json())
        .then((data)=>{
            console.log(data);
        })
    }
});