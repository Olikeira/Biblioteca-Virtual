function logout() {
    firebase.auth().signOut().then(() => {
        window.location.href = "/templates/indexprojeto.html";
    }).catch(() => {
        alert('Erro ao fazer logout');
    });
}
