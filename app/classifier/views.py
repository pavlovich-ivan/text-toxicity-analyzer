import numpy as np
import tensorflow as tf
from pathlib import Path
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .forms import CommentTextForm
from .utils import clear_text
from .models import Results

# Create your views here.
class ClassificationView(LoginRequiredMixin, TemplateView):
    template_name = 'classifier/classification.html'

    def get(self, request):
        context = {
            'form': CommentTextForm(),
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = CommentTextForm(request.POST)

        if form.is_valid():
            input_text = form.cleaned_data.get('comment_text')
            clean_text = clear_text(input_text)

            model = tf.keras.models.load_model(Path(Path(__file__).parent, 'end_to_end_48'))
            predict = model.predict(np.expand_dims(clean_text, 0))
            predict = (predict > 0.5).astype(int)

            results = Results(comment_text=input_text, toxic=predict[0][0], severe_toxic=predict[0][1], obscene=predict[0][2], threat=predict[0][3], insult=predict[0][4], identity_hate=predict[0][5])
            results.save()

            context = {
                'form': form,
                'results' : {
                    'toxic': predict[0][0],
                    'severe_toxic': predict[0][1],
                    'obscene': predict[0][2],
                    'threat': predict[0][3],
                    'insult': predict[0][4],
                    'identity_hate': predict[0][5],
                }
            }
            return render(request, self.template_name, context)
