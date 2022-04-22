document.querySelector('#items').addEventListener('wheel', function(event){
    if(event.deltaY > 0){
        event.target.scrollBy(450, 0)
    }else{
        event.target.scrollBy(-450, 0)
    }
})


