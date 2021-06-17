let number = Number(window.prompt("Enter number: "));

let table = document.getElementById("my_table")
let table_head = document.createElement("thead")
let h_tr = document.createElement("tr")
let body = document.createElement("tbody")
for (let i = 1; i <= number; i++) {
    if(i==1){
        let th = document.createElement("th")
        th.innerText = "#";
        th.scope = "col";
    h_tr.appendChild(th);
    }
    let th = document.createElement("th")
    th.innerText = i;
    th.scope = "col";
    h_tr.appendChild(th);
    let b_tr = document.createElement("tr")
    let b_th = document.createElement("th")
    b_th.innerText = i;
    b_th.scope = "row";
    b_tr.appendChild(b_th);

    for (let j = 1; j <= number; j++) {
        b_td = document.createElement("td")
        b_td.innerText = (i * j);
        b_tr.appendChild(b_td);
    }


    body.appendChild(b_tr);
}

table_head.appendChild(h_tr);
table.appendChild(table_head);
table.appendChild(body);