function addItem()
{
    const inputVal =  document.querySelector("#i1").value
    if (inputVal==="")
    {
        return;
    }
    const dItem = document.createElement("div")
    const lItem = document.createElement("li")
    const checkBox = document.createElement("input")
    const BItem = document.createElement("button")

    checkBox.type = "checkbox"
    BItem.onclick = function()
    {
        lItem.remove()
    }
    lItem.textContent = inputVal + " "
    lItem.prepend(checkBox)
    BItem.textContent = "x"
    lItem.appendChild(BItem)
    dItem.appendChild(lItem)
    document.querySelector("#u1").appendChild(dItem)

    document.querySelector("#i1").value=""
}

/*
function removeItem()
{
    const inputVal = document.querySelector("#i2").value.trim()
    const list = document.querySelector("#u1").childNodes
    for (let i=0;i<list.length;i++)
    {
        if (list[i].nodeType===1)
        {
            if (list[i].textContent.trim()===inputVal)
            {
              document.querySelector("#u1").removeChild(list[i])
            }
        }
    }
    document.querySelector("#i2").value=""
    
}
*/


function lightDark()
{
    const mode = document.querySelector("#s1").value
    if (mode==="light")
    {
        document.querySelector("body").style.backgroundImage = "radial-gradient(rgb(215, 210, 246),white)"
        document.querySelector("body").style.color = "black"
        document.querySelector("#d1").style.backgroundColor= "white"
        document.querySelector("#i1").style.backgroundColor= "white"
    }
    else if (mode==="dark")
    {
        document.querySelector("body").style.backgroundImage = "radial-gradient(rgb(53, 42, 122),grey)"
        document.querySelector("#d1").style.backgroundColor= "#2d3436"
        document.querySelector("#i1").style.backgroundColor= "rgb(47, 54, 64)"
        document.querySelector("#d1").style.color = "white"
    }
}


function showSelected(event)
{
    event.preventDefault()
    document.querySelector(".b2").classList.toggle("button-back")
    document.querySelector("body").classList.toggle("open")
}

function deleteItem(itemId)
{
    fetch("/delete-item",
        {
            method: "POST",
            headers: {
            "Content-Type": "application/json"
        },
            body: JSON.stringify({itemId:itemId}),
        }
    ).then((_res) => 
    {
        window.location.href = "/";
    });
}

