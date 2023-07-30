document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.change').forEach(function(button) {
        button.onclick = function() {
            fetch('/cart', {
                method: 'POST',
                body: JSON.stringify({
                    book: this.id,
                    state: this.dataset.state
                })    
            })
            .then(response => response.json())
            .then(result => {
                // Print result
                console.log(result)
                if (result["remove"]) {
                    const tr1 = document.getElementById(`parent${this.id}`)
                    tr1.style.animationPlayState = 'running';
                    tr1.addEventListener('animationend', () => {
                        tr1.remove()
                    })
                } else {
                    if (result['error']) {
                    Swal.fire(
                        'failed!',
                        result['error'],
                        'error')
                    }
                    document.getElementById(`p${this.id}`).innerHTML = result["quantity"]
                    document.getElementById(`total${this.id}`).innerHTML = result["price"]
                }
                document.getElementById("totalp").innerHTML = result['total']
                
            })
            
        }
    })
})