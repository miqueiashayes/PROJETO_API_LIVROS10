from flask import flask, jsonify,  resquest 

app = Flask(__name__)

livros = [
    {
        'id': 1, 
        'titulo': 'O senhor dos aneis = A sociedade do anel',
        'autor': 'J.R.R. Tolkien'
          
    },
    {
        'id': 2, 
        'titulo': 'Harry Potter e a pedra filosofal',
        'autor': 'J.K. Rowling'
   },
   {
      'id': 3, 
      'titulo': 'O hobbit',
      'autor': 'J.R.R. Tolkien'
   },
   {
       @app.route('/livros', methods=['GET'])
       def obter_livros():
        return jsonify(livros) 7

       @app.route('/livros/<int:id>', methods=['GET'])
         def obter_livro_por_id(id):
          for livro in livros:
            if  livro.get('id') == id:
                return jsonify(livro)

       @app.route('/livros/<int:id>', methods= ['GET'])
            def editar_livros_por_id(id):
                livro_alterado = request.get_json()
                for indice, livro in enumerate(livros):
                    if livro.get('id') == id:
                        livros[indice].update(livro_alterado)
                        return jsonify(livros[indice])

      @app.route('/livros', methods=['POST'])
       def incluir_novo_livro():
        novo_livro = request.get_json()
        livros.append(novo_livro)
        return jsonify(livros)

     @app.route('/livros/<int:id>', ), methods=['DELETE'])
        def excluir_livro_por_id(id):
            for indice, livro in enumerate(livros):
                if livro.get('id') == id:
                    del livros[indice]
                    return jsonify(livros) 

   } 
    
]