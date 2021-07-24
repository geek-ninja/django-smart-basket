console.log('welcome to cart');

var URL = "{% url 'flipkart:cartView'%}"
function check(){
    window.alert('ok')
    var data = {'count' : '5'}
    $.post(URL,data)
}