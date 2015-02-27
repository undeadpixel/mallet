#!/usr/bin/env bash

ROC_DATA="roc_data"

../roc_curve.py ../files/hmms/toy_model.tgf ../files/sequences/context_real_donors.raw > "$ROC_DATA/toy_model_roc.tsv"
../roc_curve.py ../files/hmms/tia1_binding_tgf/postint_u1_comp_4tia1.tgf ../files/sequences/context_real_donors.raw > "$ROC_DATA/tia1_postint_u1_comp_4tia1_roc.tsv"
../roc_curve.py ../files/hmms/u1_binding_tgf/u1_complete.tgf ../files/sequences/context_real_donors.raw > "$ROC_DATA/u1_complete_roc.tsv"
../roc_curve.py ../files/hmms/u1_binding_tgf/u1_2_8.tgf ../files/sequences/context_real_donors.raw > "$ROC_DATA/u1_2_8_roc.tsv"
../roc_curve.py ../files/hmms/u1_binding_tgf/u1_3_7.tgf ../files/sequences/context_real_donors.raw > "$ROC_DATA/u1_3_7_roc.tsv"
