"""For PyTorch"""

def model_parameters_stats(model):
    if not hasattr(model, "named_parameters"):
        return None, None, None
    trainable_params = 0
    all_params = 0
    for _, param in model.named_parameters():
        num_params = param.numel()
        if num_params == 0 and hasattr(param, "ds_numel"):
            num_params = param.ds_numel
        all_params += num_params
        if param.requires_grad:
            trainable_params += num_params
    return trainable_params, all_params, 100 * trainable_params / all_params


def model_parameters_str(model):
    if not hasattr(model, "named_parameters"):
        return None, None, None
    trainable_params = 0
    all_params = 0
    for _, param in model.named_parameters():
        num_params = param.numel()
        if num_params == 0 and hasattr(param, "ds_numel"):
            num_params = param.ds_numel
        all_params += num_params
        if param.requires_grad:
            trainable_params += num_params
    if trainable_params == all_params:
        return f"{all_params}"
    else:
        return f"{trainable_params},{all_params}"
