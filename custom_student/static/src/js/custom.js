odoo.define('custom_student.LanguageSelection', function(require){
"use strict";
var UserMenu = require('web.UserMenu');

UserMenu.include({
        init: function(){
            this._super.apply(this, arguments);
            var self = this;
            var lang_list ='';

        self._rpc({
             model: 'res.lang',
             method: 'search_read',
             domain: [],
             fields: ['name', 'code'],
             lazy: false,
        }).then(function(res){
             _.each(res, function(lang){
                var a ='<i class="fa fa-check"/>'
                lang_list += '<a>' +
                 lang['name'] + ' '+ a +'</a><br/>';
                });
                $('switch-lang').replaceWith(lang_list);
             })
        }
        })
    })