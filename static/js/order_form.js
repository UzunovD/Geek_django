"use strict";

let _quantity, _price, orderitemNum, deltaQuantity, orderitemQuantity, deltaCost;
let quantityArr = [];
let priceArr = [];
let orderTotalQuantityDOM;

// $('.order_total_quantity').html('');
// document.querySelector('.order_total_quantity').innerHTML = '';

let totalForms;
let orderTotalQuantity;
let orderTotalCost;
let orderForm;
let orderFormQuantity;
let orderFormDelete;


function parseOrderForm() {
    for (let i = 0; i < totalForms; i++) {
        orderFormQuantity = document.querySelector('input[name="orderitems-' + i + '-quantity"]');
        orderFormDelete = document.querySelector('input[name="orderitems-' + i + '-DELETE"]');
        orderFormQuantity.addEventListener('change', chengeQuantity);
        _quantity = parseInt(orderFormQuantity.value);
        if (_quantity) {
            _price = parseFloat(document.querySelector('.orderitems-' + i + '-price').innerText.replace(',', '.').match(/\d+.\d+/));
            quantityArr[i] = _quantity;
            priceArr[i] = (_price) ? _price : 0;
            orderFormDelete.addEventListener('change', formDelete);
        }
    }
}

function chengeQuantity(event) {
    orderitemNum = parseInt(event.target.name.match(/\d+/));
    if (priceArr[orderitemNum]) {
        orderitemQuantity = parseInt(event.target.value);
        deltaQuantity = orderitemQuantity - quantityArr[orderitemNum];
        quantityArr[orderitemNum] = orderitemQuantity;
        orderSummaryUpdate(priceArr[orderitemNum], deltaQuantity);
    }
}

function formDelete(event) {
        orderitemNum = parseInt(event.target.name.match(/\d+/));
        if (event.target.checked) {
            deltaQuantity = -quantityArr[orderitemNum];
        } else {
            deltaQuantity = quantityArr[orderitemNum];
        }
        orderSummaryUpdate(priceArr[orderitemNum], deltaQuantity);
    }


function orderSummaryUpdate(orderitemPrice, deltaQuantity) {
    deltaCost = orderitemPrice * deltaQuantity;
    orderTotalCost = Number((orderTotalCost + deltaCost).toFixed(2));
    orderTotalQuantity = orderTotalQuantity + deltaQuantity;

    document.querySelector('.order_total_cost').innerHTML = orderTotalCost.toString();
    orderTotalQuantityDOM.innerHTML = orderTotalQuantity.toString();
}

function deleteOrderItem(row) {
    let targetName = row[0].querySelector('input[type="number"]').name;
    orderitemNum = parseInt(targetName.replace('orderitems-', '').replace('-quantity', ''));
    deltaQuantity = -quantityArr[orderitemNum];
    orderSummaryUpdate(priceArr[orderitemNum], deltaQuantity);
}

function updateTotalQuantity() {
    for (let i = 0; i < totalForms; i++) {
        orderTotalQuantity += quantityArr[i];
        orderTotalCost += quantityArr[i] * priceArr[i];
    }
    orderTotalQuantityDOM.html(orderTotalQuantity.toString());
    document.querySelector('.order_total_cost').innerHTML(Number(orderTotalCost.toFixed(2)).toString());
}

window.onload = function () {
    orderTotalQuantityDOM = document.querySelector('.order_total_quantity');
    totalForms = parseInt(document.querySelector('input[name="orderitems-TOTAL_FORMS"]').value);
    orderTotalQuantity = parseInt(orderTotalQuantityDOM.textContent) || 0;
    orderTotalCost = parseFloat(document.querySelector('.order_total_cost').textContent.replace(',', '.')) || 0;
    orderForm = document.querySelector('.order_form ');

    parseOrderForm();

    if (!orderTotalQuantity) {
        updateTotalQuantity();
    }



    $('.formset_row').formset({
        addText: 'добавить продукт',
        deleteText: 'удалить',
        prefix: 'orderitems',
        // removed: deleteOrderItem
    });

    // orderForm.on('change', 'select', function (event) {
    //     let target = event.target;
    //     console.log(target);
    // });

};