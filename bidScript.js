var vm = new Vue({
    el: '#vBids',
    
    data: {
        button: undefined,
        chatInput: undefined,
        chatSend: undefined,
        priceInput: undefined,
        
    },
    

    methods:{
        setVars: function(){
            this.button = document.getElementsByClassName('otree-btn-next')[0]
            this.chatInput = document.getElementsByClassName("otree-chat__input")[0]
            this.chatSend = document.getElementsByClassName('otree-chat__btn-send')[0]
            this.priceInput = document.getElementById("id_bid_amount")
            window.onload = function(e){
                this.button.addEventListener("click", function() {
                    this.chatInput.value = "Bid $" + priceInput.value
                    this.chatSend.click()
                })
                
            }
            

        },


    },
    mounted(){
        this.setVars()
    }

});
