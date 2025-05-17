/**
 * app-ecommerce-product-list
 */

'use strict';

// Datatable (jquery)
$(function () {

  // Variable declaration for table
  var dt_product_table = $('.datatables-products')

  // E-commerce Products datatable
  if (dt_product_table.length) {
    var dt_products = dt_product_table.DataTable({
      
      columnDefs: [
        {
          // For Responsive
          className: 'control',
          searchable: false,
          orderable: false,
          responsivePriority: 2,
          targets: 0,
          render: function (data, type, full, meta) {
            return '';
          }
        },
        {
          // For Checkboxes
          targets: 1,
          orderable: false,
          checkboxes: {
            selectAllRender: '<input type="checkbox" class="form-check-input">'
          },
          render: function () {
            return '<input type="checkbox" class="dt-checkboxes form-check-input" >';
          },
          searchable: false
        },
        {
          // Product name and product_brand
          targets: 2,
          responsivePriority: 1,
        },
        {
          // Product Category
          targets: 3,
          responsivePriority: 5,
        },
        {
          // Stock
          targets: 4,
          orderable: false,
          responsivePriority: 3,
        },
        {
          // cantidad
          targets: 5,
        },
        {
          // precio
          targets: 6,
        },
        {
          // status
          targets: 7,
        },
      ],
    });
  }
});
