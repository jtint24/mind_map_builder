from typing import List, Tuple, Set
from transformers import AutoTokenizer, AutoModel
import transformers
import torch

class RelationExtractor:
    """
    RelationExtractor

    This class is responsible for getting the list of related keywords in a text from the list of keywords and the
    original text.
    """

    def __init__(self, threshold: float = 0.05):
        transformers.logging.set_verbosity_error()
        self.encoding_length = 384
        self.threshold = threshold
        self.model = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
        self.tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
        self.embeddings_cache = {}

    def __call__(self, keywords: List[str]) -> Set[Tuple[str, str]]:
        return self.get_relationship_set(keywords)

    def get_encoding(self, text: str) -> List[float]:
        if text not in self.embeddings_cache:
            inputs = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True)
            with torch.no_grad():
                outputs = self.model(**inputs)
            self.embeddings_cache[text] = outputs.last_hidden_state.mean(dim=1).squeeze().tolist()

        return self.embeddings_cache[text]

    def get_similarity_score(self, vec_a: List[float], vec_b: List[float]) -> float:
        products = [a * b for a, b in zip(vec_a, vec_b)]
        product_sum = 0
        for term in products:
            product_sum += term

        return product_sum

    def get_relationship_set(self, keywords: List[str]) -> Set[Tuple[str, str]]:
        ret_set = set()

        for sig_keyword_idx in range(len(keywords)):
            sig_keyword = keywords[sig_keyword_idx]
            for inf_keyword_idx in range(sig_keyword_idx + 1, len(keywords)):
                inf_keyword = keywords[inf_keyword_idx]
                sig_embedding = self.get_encoding(sig_keyword)
                inf_embedding = self.get_encoding(inf_keyword)
                similarity = self.get_similarity_score(sig_embedding, inf_embedding)
                if similarity > self.threshold * self.encoding_length:
                    ret_set.add((sig_keyword, inf_keyword))
        return ret_set
