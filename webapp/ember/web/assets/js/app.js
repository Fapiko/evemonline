window.App = Ember.Application.create();

App.Router.map(function () {
  this.resource('evemonline', { path: '/' });
});

App.HomeRouter = Ember.Route.extend({
    renderTemplate: function() {
        this.render({ outlet: 'main' });
    }
});
