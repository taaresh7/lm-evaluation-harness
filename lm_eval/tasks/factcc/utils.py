import datasets
def process_docs(dataset: datasets.Dataset):
    def _helper(doc):
      # modifies the contents of a single
      # document in our dataset.
      doc["choices"] = list(set(dataset['expected']))
      doc["gold"] = doc["expected"]
      doc["prompt"] = doc["messages"][0]["content"] + "\n" + doc["messages"][1]["content"] 
      return doc

    return dataset.map(_helper) # returns back a datasets.Dataset object