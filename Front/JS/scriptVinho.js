/*
  --------------------------------------------------------------------------------------
  Função para obter a lista existente do servidor via requisição GET
  --------------------------------------------------------------------------------------
*/
const getList = async () => {
    let url = 'http://127.0.0.1:5000/vinhos';
    fetch(url, {
      method: 'get',
    })
      .then((response) => response.json())
      .then((data) => {
        data.vinhos.forEach(item => insertList(item.name, item.fixed_acidity, item.volatile_acidity, item.citric_acid, item.residual_sugar, item.chlorides,
          item.free_sulfur_dioxide, item.total_sulfur_dioxide, item.density, item.pH, item.sulphates, item.alcohol, item.quality))
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  }
  
  /*
    --------------------------------------------------------------------------------------
    Chamada da função para carregamento inicial dos dados
    --------------------------------------------------------------------------------------
  */
  getList()
  
  /*
    --------------------------------------------------------------------------------------
    Função para colocar um item na lista do servidor via requisição POST
    --------------------------------------------------------------------------------------
  */
  const postItem = async (inputName, inputFixed_acidity, inputVolatile_acidity, inputCitric_acid, inputResidual_sugar, inputChlorides, inputFree_sulfur_dioxide,
    inputTotal_sulfur_dioxide, inputDensity, inputpH, inputSulphates, inputAlcohol) => {
    const formData = new FormData();
    formData.append('name', inputName);
    formData.append('fixed_acidity', inputFixed_acidity);
    formData.append('volatile_acidity', inputVolatile_acidity);
    formData.append('citric_acid', inputCitric_acid);
    formData.append('residual_sugar', inputResidual_sugar);
    formData.append('chlorides', inputChlorides);
    formData.append('free_sulfur_dioxide', inputFree_sulfur_dioxide);
    formData.append('total_sulfur_dioxide', inputTotal_sulfur_dioxide);
    formData.append('density', inputDensity);
    formData.append('pH', inputpH);
    formData.append('sulphates', inputSulphates);
    formData.append('alcohol', inputAlcohol);
  
    let url = 'http://127.0.0.1:5000/vinho';
    fetch(url, {
      method: 'post',
      body: formData
    })
      .then((response) => response.json())
      .catch((error) => {
        console.error('Error:', error);
      });
  }
  
  /*
    --------------------------------------------------------------------------------------
    Função para deletar um item da lista do servidor via requisição DELETE
    --------------------------------------------------------------------------------------
  */
  const deleteItem = (item) => {
    console.log(item)
    let url = 'http://127.0.0.1:5000/vinho?name=' + item;
    fetch(url, {
      method: 'delete'
    })
      .then((response) => response.json())
      .catch((error) => {
        console.error('Error:', error);
      });
  }

  /*
  --------------------------------------------------------------------------------------
  Função para adicionar um novo Vinho
  --------------------------------------------------------------------------------------
*/

const adicionarVinho = () => {
    let inputName = document.getElementById("newName").value;
    let inputFixed_acidity = document.getElementById("newFixed_acidity").value;
    let inputVolatile_acidity = document.getElementById("newVolatile_acidity").value;
    let inputCitric_acid = document.getElementById("newCitric_acid").value;
    let inputResidual_sugar = document.getElementById("newResidual_sugar").value;
    let inputChlorides = document.getElementById("newChlorides").value;
    let inputFree_sulfur_dioxide = document.getElementById("newFree_sulfur_dioxide").value;
    let inputTotal_sulfur_dioxide = document.getElementById("newTotal_sulfur_dioxide").value;
    let inputDensity = document.getElementById("newDensity").value;
    let inputpH = document.getElementById("newpH").value;
    let inputSulphates = document.getElementById("newSulphates").value;
    let inputAlcohol = document.getElementById("newAlcohol").value;



    if ((0 <= inputFixed_acidity) &&
        (0 <= inputVolatile_acidity) && 
        (0 <= inputCitric_acid) && 
        (0 <= inputResidual_sugar) &&
        (0 <= inputChlorides) && 
        (0 <= inputFree_sulfur_dioxide) &&
        (0 <= inputTotal_sulfur_dioxide) &&
        (0 < inputDensity) &&
        (0 <= inputpH) && (inputpH <= 14) &&
        (0 <= inputSulphates) &&
        (0 <= inputAlcohol)) {

          // Verifica se a vinho com o mesmo nome
          const checkVinho = 'http://127.0.0.1:5000/vinhos?name=' + inputName;
          fetch(checkVinho, {
          method: 'get'
          })
          .then((response) => response.json())
          .then((data) => 
          {
            if (data.vinhos && data.vinhos.some(item => item.name === inputName)) 
            {
              alert ("O vinho já está cadastrado");
            } 
            else if ((inputName === '')||(inputFixed_acidity === '')||(inputVolatile_acidity === '')||(inputCitric_acid === '')||(inputResidual_sugar === '')
              ||(inputChlorides === '')||(inputFree_sulfur_dioxide === '')||(inputTotal_sulfur_dioxide === '')||(inputDensity === '')||(inputpH === '')
              ||(inputSulphates === '')||(inputAlcohol === '')) 
            {
              alert("Dados do vinho estão faltando!");
            } 
            else if (isNaN((inputFixed_acidity === '')||(inputVolatile_acidity === '')||(inputCitric_acid === '')||(inputResidual_sugar === '')||(inputChlorides === '')
                    ||(inputFree_sulfur_dioxide === '')||(inputTotal_sulfur_dioxide === '')||(inputDensity === '')||(inputpH === '')||(inputSulphates === '')
                    ||(inputAlcohol === '')))
            {
              alert("Todos os dados, exceto nome, são números!");
            } 
            else 
            {
              insertList(inputName, inputFixed_acidity, inputVolatile_acidity, inputCitric_acid, inputResidual_sugar, inputChlorides, inputFree_sulfur_dioxide,
                inputTotal_sulfur_dioxide, inputDensity, inputpH, inputSulphates, inputAlcohol)
              postItem(inputName, inputFixed_acidity, inputVolatile_acidity, inputCitric_acid, inputResidual_sugar, inputChlorides, inputFree_sulfur_dioxide,
                inputTotal_sulfur_dioxide, inputDensity, inputpH, inputSulphates, inputAlcohol)
              alert("Vinho adicionado!")
            }
          })
          .catch((error) => {
            console.error('Error:', error);
          });
    }
    else {
      alert("Dados de entrada invalidos!")
    }


}


/*
  --------------------------------------------------------------------------------------
  Função para inserir items na lista apresentada
  --------------------------------------------------------------------------------------
*/
const insertList = (name, fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH,
  sulphates, alcohol, quality) => {
    var item = [name, fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH,
      sulphates, alcohol, quality]
    var table = document.getElementById('Tabela_de_vinho');
    var row = table.insertRow();
  
    for (var i = 0; i < item.length; i++) {
      var cel = row.insertCell(i);
      cel.textContent = item[i];
    
    }
    insertButton(row.insertCell(-1))
    document.getElementById("newName").value = "";
    document.getElementById("newFixed_acidity").value = "";
    document.getElementById("newVolatile_acidity").value = "";
    document.getElementById("newCitric_acid").value = "";
    document.getElementById("newResidual_sugar").value = "";
    document.getElementById("newChlorides").value = "";
    document.getElementById("newFree_sulfur_dioxide").value = "";
    document.getElementById("newTotal_sulfur_dioxide").value = "";
    document.getElementById("newDensity").value = "";
    document.getElementById("newpH").value = "";
    document.getElementById("newSulphates").value = "";
    document.getElementById("newAlcohol").value = "";
  
    removeElement()
  }

/*
  --------------------------------------------------------------------------------------
  Função para criar um botão close para cada item da lista
  --------------------------------------------------------------------------------------
*/
const insertButton = (parent) => {
    let span = document.createElement("span");
    let txt = document.createTextNode("\u00D7");
    span.className = "close";
    span.appendChild(txt);
    parent.appendChild(span);
  }


/*
  --------------------------------------------------------------------------------------
  Função para remover um item da lista de acordo com o click no botão close
  --------------------------------------------------------------------------------------
*/
const removeElement = () => {
    let close = document.getElementsByClassName("close");
    // var table = document.getElementById('Tabela_de_vinho');
    let i;
    for (i = 0; i < close.length; i++) {
      close[i].onclick = function () {
        let div = this.parentElement.parentElement;
        const nomeItem = div.getElementsByTagName('td')[0].innerHTML
        if (confirm("Você tem certeza?")) {
          div.remove()
          deleteItem(nomeItem)
          alert("Removido!")
        }
      }
    }
  }
  
  /*
  --------------------------------------------------------------------------------------
  Verifica entrada de dados
  --------------------------------------------------------------------------------------
  */





