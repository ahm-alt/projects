
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.add').forEach(function(button) {
        button.onclick = function() {
            if (this.id !== "none"){
                
                Swal.fire(
                    'Done!',
                    'Add to cart successfully!',
                    'success'
                )           
                fetch('/cart', {
                    method: 'POST',
                    body: JSON.stringify({
                        book: this.id,
                        state: 'add'
                    })    
                })
            } else {
                Swal.fire(
                    'failed!',
                    'you have to sign in',
                    'error',
                )       
            }
        }
    })


})



