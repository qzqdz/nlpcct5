# coding=utf-8
# Copyright 2018 The Google AI Language Team Authors and The HuggingFace Inc. team.
# Copyright (c) 2018, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#	 http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os

try:
	from scipy.stats import pearsonr, spearmanr
	from sklearn.metrics import matthews_corrcoef, f1_score,recall_score


	_has_sklearn = True
except (AttributeError, ImportError):
	_has_sklearn = False


def is_sklearn_available():
	return _has_sklearn

import numpy as np

if _has_sklearn:

	def simple_accuracy(preds, labels):
		print(preds)
		print('------------------------------------')
		print(labels)
		print('------------------------------------')
		print(preds == labels)
		return (preds == labels).mean()

	def acc_and_f1(preds, labels):
		acc = simple_accuracy(preds, labels)
		f1 = f1_score(y_true=labels, y_pred=preds)
		return {
			"acc": acc,
			"f1": f1,
			"acc_and_f1": (acc + f1) / 2,
		}

	def pearson_and_spearman(preds, labels):
		pearson_corr = pearsonr(preds, labels)[0]
		spearman_corr = spearmanr(preds, labels)[0]
		return {
			"pearson": pearson_corr,
			"spearmanr": spearman_corr,
			"corr": (pearson_corr + spearman_corr) / 2,
		}
	def sigmoid_function(x):
		return 1/(1+np.exp(-x))
	def glue_compute_metrics(task_name, preds, labels):
		assert len(preds) == len(labels)
		if task_name == "cola":
			return {"mcc": matthews_corrcoef(labels, preds)}
		elif task_name == "sst-2":
			return {"acc": simple_accuracy(preds, labels)}
		elif task_name == "mrpc":
			return acc_and_f1(preds, labels)
		elif task_name == "sts-b":
			return pearson_and_spearman(preds, labels)
		elif task_name == "qqp":
			return acc_and_f1(preds, labels)
		elif task_name == "mnli":
			return {"acc": simple_accuracy(preds, labels)}
		elif task_name == "mnli-mm":
			return {"acc": simple_accuracy(preds, labels)}
		elif task_name == "qnli":
			return {"acc": simple_accuracy(preds, labels)}
		elif task_name == "rte":
			return {"acc": simple_accuracy(preds, labels)}
		elif task_name == "wnli":
			return {"acc": simple_accuracy(preds, labels)}
		elif task_name == "hans":
			return {"acc": simple_accuracy(preds, labels)}
		elif task_name == "desccls":
			return {"acc": simple_accuracy(preds, labels)}

		elif task_name == 'allnlpcct5' or task_name == 'nlpcct5level1' or task_name == 'nlpcct5level2' or task_name == 'nlpcct5level3'  or task_name == 'reuters':

			# sigmoid_preds = preds
			sigmoid_preds = sigmoid_function(preds)
			sigmoid_preds = np.greater(sigmoid_preds,0.5).astype(np.int32)
			macro_r = recall_score(labels, sigmoid_preds,average='macro')
			micro_r = recall_score(labels, sigmoid_preds, average='micro')

			macro_f1 = f1_score(labels,sigmoid_preds,average='macro')
			micro_f1 = f1_score(labels, sigmoid_preds, average='micro')

			if not os.path.exists('./eval_res/'):
				os.mkdir('./eval_res/')

			with open(r'./eval_res/labels.txt','w',encoding='utf-8') as f:
				f.write(str(labels.tolist()))
			with open(r'./eval_res/pred.txt','w',encoding='utf-8') as f:
				f.write(str(sigmoid_preds.tolist()))

			return {
				'acc':simple_accuracy(sigmoid_preds,labels),
				'macro_r': macro_r,
				'micro_r': micro_r,
				'macro_f1':macro_f1,
				'micro_f1':micro_f1,
			}

		else:
			raise KeyError(task_name)


	def xnli_compute_metrics(task_name, preds, labels):
		assert len(preds) == len(labels)
		if task_name == "xnli":
			return {"acc": simple_accuracy(preds, labels)}
		else:
			raise KeyError(task_name)
