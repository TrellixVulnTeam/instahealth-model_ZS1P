import sentencepiece as spm

spm.SentencePieceTrainer.train('--input=botchan.txt --model_prefix=spiece --vocab_size=2000')

s = spm.SentencePieceProcessor()
s.load("spiece.model")

for n in range(5):
	print(s.encode('New York', out_type=str, enable_sampling=True, alpha=0.1, nbest_size=-1))