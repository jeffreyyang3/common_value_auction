var vm = new Vue({ //todo: clean up code, comment
    delimiters: ['{(', ')}'],
    el: '#vBids',
    
    data: {
        chatMessages: [],
     
        yourTurn: false,
        sequential: true,
        chatNames: [],


        bidAmounts: [],
        displayRange:  9999999,
        

    },


    watch:{
        chatNames: function(){
            console.log("asfdsadf")
            function mean(numbers){
                var total = 0, i;
                for (i = 0; i < numbers.length; i += 1) {
                    total += numbers[i];
                }
                return total / numbers.length;
            }
            function median(numbers){
                var median = 0, numsLen = numbers.length;
                temp = numbers.slice(0)
            
                if (numsLen % 2 === 0) {
                    // average of two middle numbers
                    median = (temp[numsLen / 2 - 1] + temp[numsLen / 2]) / 2;
                } else { // is odd
                    // middle number only
                    median = temp[(numsLen - 1) / 2];
                }

                return median;
            }
            //console.log(this.chatNames)
         
            //inefficient but who cares
            this.bidAmounts = []
            for(let i = 0; i < this.chatNames.length; i++){
                this.bidAmounts.push(parseInt(this.bids[i].innerText))
            }
            if(this.bidAmounts.length > displayRange){
                this.bidMean = mean(this.bidAmounts.slice(bidAmounts.length - displayRange, bidAmounts.length))
                this.bidMedian = median(this.bidAmounts.slice(bidAmounts.length - displayRange, bidAmounts.length))
            }
            else{
                this.bidMean = mean(this.bidAmounts)
                this.bidMedian = median(this.bidAmounts)
            }
            meanDisplay = document.getElementById("meanDisplay")
            medianDisplay = document.getElementById("medianDisplay")
            meanDisplay.innerText = `Mean of the last ${this.displayRange} values: ${this.bidMean}`
            medianDisplay.innerText = `Median of the last ${this.displayRange} values: ${this.bidMedian}`
          


   
            if(this.chatNames.length >= parseInt(this.playerNumber) - 1){
                this.yourTurn = true
            }
            else{
                queuePosition = document.getElementById('position')

                queuePosition.innerText = parseInt(this.playerNumber) - this.chatNames.length - 1
            }

      

       
        }

    },

    methods:{
     
        
        setVars: function(){

            this.chatNames = document.getElementsByClassName("otree-chat__nickname")
            this.bids = document.getElementsByClassName("otree-chat__body")
            this.displayRange = parseInt(document.getElementById("displayRange").value)


            
            
            this.button = document.getElementsByClassName('otree-btn-next')[0]
            
            this.chatInput = document.getElementsByClassName("otree-chat__input")[0]
            this.chatSend = document.getElementsByClassName('otree-chat__btn-send')[0]
            this.priceInput = document.getElementById("id_bid_amount")
            this.playerNumber = parseInt(document.getElementById("playerName").value)
            this.sequential = document.getElementById("sequential").value
            this.sequential = this.sequential == "True" 
            this.showStats = document.getElementById("showStats").value
            this.showStats = this.showStats == "True" 
            
            
            
            if(this.playerNumber == 1){
                this.yourTurn = true

            }
            this.button.addEventListener("click", function() {
                console.log("clicked")
                vm.chatInput.value = vm.priceInput.value
                
                //vm.chatInput.value = "Bid $" + vm.priceInput.value
                vm.chatSend.click()
                
            })
            
            
           
            

        },
        
        arrayOps: function(){
            setInterval(
                function(){
      
                    messages = []
                    for(let i = 0; i < vm.chatMessages.length; i++){
                        messages.push(vm.chatMessages[i].innerText.slice(7))
                    }
                    vm.chatNames = messages
                
                    
           

                }, 300)
            
        } 
        


    },
    mounted(){
        console.log("asdfdsa")
        this.setVars()
        this.arrayOps()
   
    }

});







