/* const searchfield = document.getElementById('search');

const productOutput = document.getElementById('product-wrap');
productOutput.style.display ='none';
const productTable = document.getElementById('def-products');
const productWrap = document.getElementById('product-wrap-2');
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
            if (data.length === 0) {
                productOutput.style.display='block';
                productOutput.innerHTML='no data to display';
                productTable.style.display = 'none';
            }
            else{
                data.forEach(element => {
                    productWrap.innerHTML +=`
                <div class="product-wrap" >
                            <div class="product text-center">
                                <figure class="product-media">
                                    <a href="product-default.html">
                                        <img src={{product.photo.url}} alt="Product" width="300"
                                            height="338" />
                                    </a>
                                    <div class="product-action-horizontal">
                                        <a data-product="{{product.id}}" data-action="add" class="btn btn-primary update-cart btn-product-icon btn-cart w-icon-cart" 
                                            title="Add to cart"></a>   
                                    </div>
                                </figure>
                                <div class="product-details">
                                    <div class="product-cat">
                                        <a href="shop-banner-sidebar.html">
                                            {% for cat in product.category.all %}
                                            {{cat.name}}
                                            {%endfor%}
                                            
                                        </a>
                                    </div>
                                    <h3 class="product-name">
                                        <a href="{% url 'product_details' product.id %}">${element.title}</a>
                                    </h3>
                                    <div class="ratings-container">
                                        <div class="ratings-full">
                                            <span class="ratings" style="width: 100%;"></span>
                                            <span class="tooltiptext tooltip-top"></span>
                                        </div>
                                        <a href="product-default.html" class="rating-reviews">(3 reviews)</a>
                                    </div>
                                    <div class="product-pa-wrapper">
                                        <div class="product-price">
                                            {{product.price}}$
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>

                `
                });
                
            }
        });
    }
    else{
        productOutput.style.display='none';
        productTable.style.display = 'block';

    }
}); */