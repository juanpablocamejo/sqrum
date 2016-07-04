var app = angular.module('app', ['angular.filter'], function($httpProvider) {
    // Use x-www-form-urlencoded Content-Type
    $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8';
});

app.directive('menu', function() {
  return {
    restrict: 'E',
    templateUrl:"menu.html"
  };
});

app.directive('userstory', function() {
  return {
    restrict: 'E',
    templateUrl:"us.html"
  };
});


/// SERVICIOS
app.service('DATA', function() {
    this.prioridades = [
        { id: "1", nombre: "Baja"}, 
        { id: "2", nombre: "Normal" }, 
        { id: "3", nombre: "Alta" }
    ];
    this.estados = [
        { id: "1", nombre: "Pendiente"}, 
        { id: "2", nombre: "En desarrollo"}, 
        { id: "3", nombre: "Terminado" },
        { id: "4", nombre: "Validado" }
    ];
});
app.service('API', function($http) {
    
    function submit(url, dto, type) {
        var req = {
            method: type,
            url: url,
            data: dto,
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            transformRequest: function(obj) {
                var str = [];
                for (var p in obj)
                    str.push(encodeURIComponent(p) + "=" + encodeURIComponent(obj[p]));
                return str.join("&");
            }
        };

        return $http(req);
    }
    
    this.GET = function(res) {
        return $http.get(res);
    }

    this.POST = function(url, dto) {
        return submit(url, dto, 'POST');
    }

    this.PUT = function(url, dto) {
        return submit(url, dto, 'PUT');
    }

    this.DELETE = function(url) {
        var req = {
            method: 'DELETE',
            url: url,
        };
        return $http(req);
    };
});

//Funciones de carga desde la API
function CargarRoles(API, scp, key) {
    return API.GET('/api/rol').then(function(resp) {
        scp[key] = resp.data;
    });
}

function CargarDesarrolladores(API, scp, key) {
    return API.GET('/api/desarrollador').then(function(resp) {
        scp[key] = resp.data;
    });
}

function CargarIteraciones(API, scp, key) {
    return API.GET('/api/iteracion').then(function(resp) {
        scp[key] = resp.data;
        scp['cb' + key] =[];
        for(var i in resp.data){
            scp['cb' + key][i] = {id:resp.data[i].id, nombe:resp.data[i].nombre};
        }
    });
}

function CargarStories(API, scp, key) {
    return API.GET('/api/user_story/').then(function(resp) {
         scp[key] = ngDTO(resp.data,scp);
    });
}


/// CONTROLLERS
function TableroCtrl($scope, API, DATA,$window) {
    $scope.prioridades = DATA.prioridades;
    $scope.estados = DATA.estados;
    CargarDesarrolladores(API, $scope, "desarrolladores");
    CargarIteraciones(API, $scope, "iteraciones")
    CargarRoles(API, $scope, "roles").then(function(){
        CargarStories(API, $scope, "us");
    });
    
    $scope.fdt = function (d) {
        var arr = d.split('-');
        var res = arr[2] + '-' + arr[1] + '-' + arr[0];
        return res;
    };
    
    $scope.editUS = function(u, b){
        API.PUT('/api/user_story/' + u.id,apiDTO(u)).then(
            function(){ console.log('EDIT US N°' + u.id +': -> OK');},
            function(resp){ console.log('EDIT US -> ERROR:');console.log(resp);}
        )
    };

    $scope.deleteUS = function(i, us_id){
        if (confirm("¿Está seguro de eliminar la User Story?")){
        API.DELETE('/api/user_story/' + us_id).then(
            function(){ console.log('DELETE US N°' + us_id +': -> OK'); $scope.us.splice(i,1);},
            function(resp){ console.log('DELETE US N°' + us_id +'-> ERROR:');console.log(resp);}
        );
        }
    };
}

app.controller('TableroCtrl', TableroCtrl);

function AltaUserStoryCtrl($scope, API, DATA) {
    $scope.prioridades = DATA.prioridades;
    //$scope.estados = sqDATA.estados;
    CargarRoles(API, $scope, "roles");

    //Selección inicial
    $scope.dto = {
        rol_id: {
            id: '',
            nombre: 'Seleccione...'
        },
        prioridad: $scope.prioridades[1]
    };

    $scope.CrearUS = function() {
        API.POST("api/user_story/", apiDTO($scope.dto))
            .then(function(resp) {
                    alert("User Story n° " + resp.data.id + " creada correctamente.");
                    location.reload();
                },
                function(resp) {
                    alert("Error al intentar crear la User Story." + JSON.stringify(resp.data));
                }
            );
    };
}
app.controller('AltaUserStoryCtrl', AltaUserStoryCtrl);

function AltaRolesCtrl($scope, API,$window) {
    $scope.CrearRol = function() {
        API.POST("api/rol/", apiDTO($scope.dto))
            .then(function(resp) {
                    alert("Rol N° " + resp.data.id + " creado correctamente.");
                    $window.location.reload();
                },
                function(resp) {
                    alert("Error al intentar crear un rol nuevo." + JSON.stringify(resp.data));
                }
            );
    };
}
app.controller('AltaRolesCtrl', AltaRolesCtrl);


function TableroRolesCtrl($scope, API, DATA) {
    CargarRoles(API, $scope, "roles");
    
    $scope.editRoles = function(u){
        API.PUT('/api/rol/' + u.id,apiDTO(u)).then(
            function(){ console.log('EDIT ROL N°' + u.id +': -> OK');},
            function(resp){ console.log('EDIT ROL -> ERROR:');console.log(resp);}
        )
    };
    
    $scope.deleteRoles = function(i, rol_id){
        if (confirm("¿Está seguro de eliminar el rol?")){
        API.DELETE('/api/rol/' + rol_id).then(
            function(){ console.log('DELETE ROL N°' + rol_id +': -> OK'); $scope.us.splice(i,1);},
            function(resp){ console.log('DELETE ROL N°' + rol_id +'-> ERROR:');console.log(resp);}
        );
        }
    };
}
app.controller('TableroRolesCtrl', TableroRolesCtrl);

//FUNCIONES AUXILIARES

function apiDTO(obj) {
    var res = {}
    for (var k in obj) {
        if (obj[k] && typeof(obj[k]) == "object" && "id" in obj[k]) {
            res[k] = obj[k].id;
        }
        else {
            res[k] = obj[k];
        }
    }
    return res;
}

// reemplaza los miembros de un apiDTO que sean IDs, por el json de la forma {id: nombre:}.
// para facilitar el binding bidireccional de los campos tipo "select".
function ngDTO(obj, scp) {
    if (angular.isArray(obj)){ return ngDTOArr(obj,scp);}
    var res = {};
    for (var k in obj) {
       switch(k){
            case "estado_id":
                res['estado'] = getById(obj[k],scp.estados);
                break;
            case "rol_id":
                res['rol'] = getById(obj[k],scp.roles);
                break;
            case "prioridad":
                res['prioridad'] = getById(obj[k],scp.prioridades);
                break;
            case "iteracion_id":
                res['iteracion'] = getById(obj[k],scp.iteraciones);
                break;
            case "desarrollador_id":
                res['desarrollador'] = getById(obj[k],scp.desarrolladores);
                break;
            default:
                res[k] = obj[k];
            }
    }
    return res;
}

function getById(id, arr){
    for(var i in arr){
        if (arr[i]['id']==id) {return arr[i];}
    }
    return null;
}

function ngDTOArr(arr,scp){
    var res = [];
    for (var i in arr){
        res[i] = ngDTO(arr[i],scp);
    }
    return res;
}