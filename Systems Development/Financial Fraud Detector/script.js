//The regression model formula used in the function below was developed by Rasa Kanapickiene and Zivile Grundiene. It was presented in their article "The Model of Fraud Detection in Financial Statements by Means of Financial Ratios" in 2015.

//Function to assess user's input as fraudulent or non-fraudulent
function FraudFunction(){

    // Get user input and assign it to a constant variable
    const inventory = document.getElementById("inventory").value
    const cash = document.getElementById("cash").value
    const totalAssets = document.getElementById("total-assets").value
    const sales = document.getElementById("sales").value
    const fixedAssets = document.getElementById("fixed-assets").value
    const totalLiabilities = document.getElementById("total-liabilities").value
    const currentLiabilities = document.getElementById("current-liabilities").value

    //Declaring the constant "x" representing the exponent from the regression model formula 
    const x = 5.768-4.263*inventory/totalAssets -0.029*sales/fixedAssets- 
    4.766*totalLiabilities/totalAssets -1.936*cash/currentLiabilities
    
    //Declaring the constant "p" representing the rest of the formula and plugging x into it
    const p = 1/(1+ Math.exp(x))

    //Declaring the constant "result" that will show the verdict to the user
    const result = document.getElementById("detector-result")

    // Giving conditions for the verdict
    if(p > 0.5){
        result.innerHTML = "The company's financial statements appear to be fraudulent with a Fraud Probability of: " + 100*p.toFixed(2) + "%."
    }

    else if(p<0.5){
        result.innerHTML = "The company's financial statements appear to be non-fraudulent with a Fraud Probability of: " + 100*p.toFixed(2) + "%."
    }
    
}


//Function to automatically enter the data of a fraudulent company into the number boxes when the button "Fraudulent Data Example" is pressed
function FraudExample(){
  
    // Declaring the constant variables used in the formula
    const inventory = document.getElementById("inventory")
    const cash = document.getElementById("cash")
    const totalAssets = document.getElementById("total-assets")
    const sales = document.getElementById("sales")
    const fixedAssets = document.getElementById("fixed-assets")
    const totalLiabilities = document.getElementById("total-liabilities")
    const currentLiabilities = document.getElementById("current-liabilities")

    //Set the values of the constants to those of a fraudulent company
    inventory.value = 500;
    cash.value = 300;
    totalAssets.value = 1000;
    sales.value = 350;
    fixedAssets.value = 100;
    totalLiabilities.value = 450;
    currentLiabilities.value = 250;

    //Declaring the constant "x" representing the exponent from the regression model formula 
    const x = 5.768-4.263*inventory/totalAssets -0.029*sales/fixedAssets- 
    4.766*totalLiabilities/totalAssets -1.936*cash/currentLiabilities
    
    //Declaring the constant "p" representing the rest of the formula and plugging x into it
    const p = 1/(1+ Math.exp(x))

    //Declaring the constant "result" that will show the verdict to the user
    const result = document.getElementById("detector-result")

    // Giving conditions for the verdict
    if(p > 0.5){
        result.innerHTML = "The company's financial statements appear to be fraudulent with a Fraud Probability of: " + 100*p.toFixed(2) + "%."
    }

    else if(p<0.5){
        result.innerHTML = "The company's financial statements appear to be non-fraudulent with a Fraud Probability of: " + 100*p.toFixed(2) + "%."
    }    
}


//Function to automatically enter the data of a non-fraudulent company into the number boxes when the button "Non-Fraudulent Data Example" is pressed
function NoFraudExample(){
  
    //  Declaring the constant variables used in the formula
    const inventory = document.getElementById("inventory")
    const cash = document.getElementById("cash")
    const totalAssets = document.getElementById("total-assets")
    const sales = document.getElementById("sales")
    const fixedAssets = document.getElementById("fixed-assets")
    const totalLiabilities = document.getElementById("total-liabilities")
    const currentLiabilities = document.getElementById("current-liabilities")

    //Set the values of the constant to those of a non-fraudulent company
    inventory.value = 100;
    cash.value = 500;
    totalAssets.value = 3000;
    sales.value = 150;
    fixedAssets.value = 360;
    totalLiabilities.value = 800;
    currentLiabilities.value = 500;

    //Declaring the constant "x" representing the exponent from the regression model formula 
    const x = 5.768-4.263*inventory/totalAssets -0.029*sales/fixedAssets- 
    4.766*totalLiabilities/totalAssets -1.936*cash/currentLiabilities
    
    //Declaring the constant "p" representing the rest of the formula and plugging x into it
    const p = 1/(1+ Math.exp(x))

    //Declaring the constant "result" that will show the verdict to the user
    const result = document.getElementById("detector-result")

    // Giving conditions for the verdict
    if(p > 0.5){
        result.innerHTML = "The company's financial statements appear to be fraudulent with a Fraud Probability of: " + 100*p.toFixed(2) + "%."
    }

    else if(p<0.5){
        result.innerHTML = "The company's financial statements appear to be non-fraudulent with a Fraud Probability of: " + 100*p.toFixed(2) + "%."
    }
    
}

//Function to clear input boxes and result field when the button "clear form" is pressed
function Clear() {

  //Assign the user input to constant
  const inventory = document.getElementById("inventory")
  const cash = document.getElementById("cash")
  const totalAssets = document.getElementById("total-assets")
  const sales = document.getElementById("sales")
  const fixedAssets = document.getElementById("fixed-assets")
  const totalLiabilities = document.getElementById("total-liabilities")
  const currentLiabilities = document.getElementById("current-liabilities")
  const result = document.getElementById("detector-result")
  
  //Clear input and result fields by setting values to 'empty'
  inventory.value = '';
  cash.value = '';
  totalAssets.value = '';
  sales.value = '';
  fixedAssets.value = '';
  totalLiabilities.value = '';
  currentLiabilities.value = '';
  result.innerHTML = "";
}
