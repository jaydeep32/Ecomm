cartForm = document.getElementById("cart-form")


cartForm.addEventListener('submit', (e)=>{
    e.preventDefault()
    data = $(cartForm).serializeArray()

    $.ajax({
        type: "POST",
        url: $(cartForm).prop("action"),
        data:data,
        success: function(res){
            console.log(res)
        },
        error: function (err){
            console.log(err.responseText)
        }
    })

})

