from flask import Flask, request, render_template
from src import qa_model

app = Flask(__name__)


@app.route('/', methods=['POST'])
def post_answer():
    context = request.form['context']
    question = request.form['question']
    if question and context:
        answer = qa_model(context=context, question=question)
        return render_template('platform.html',
                               context=context,
                               question=question,
                               answer=answer['answer'],
                               score=round(answer['score'], 4))
    return render_template('platform.html', context=None, question=None, answer=None)


@app.route('/')
def box_render():
    return render_template('platform.html', context=None, question=None, answer=None)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8020)
