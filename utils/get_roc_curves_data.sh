#!/usr/bin/env bash

ROC_DATA="roc_data"

../scripts/roc_curve.py ../files/hmms/toy_model.tgf ../files/sequences/context_real_donors.raw > "$ROC_DATA/toy_model_roc.tsv"
../scripts/roc_curve.py ../files/hmms/tia1_binding_tgf/postint_u1_comp_4tia1.tgf ../files/sequences/context_real_donors.raw > "$ROC_DATA/tia1_postint_u1_comp_4tia1_roc.tsv"
../scripts/roc_curve.py ../files/hmms/tia1_binding_tgf/u1_comp_4tia1.tgf ../files/sequences/context_real_donors.raw > "$ROC_DATA/u1_comp_4tia1.tsv"
../scripts/roc_curve.py ../files/hmms/tia1_binding_tgf/small_prob_4TIA1.tgf ../files/sequences/context_real_donors.raw > "$ROC_DATA/small_prob_4TIA1.tsv"
../scripts/roc_curve.py ../files/hmms/u1_binding_tgf/u1_complete.tgf ../files/sequences/context_real_donors.raw > "$ROC_DATA/u1_complete_roc.tsv"
../scripts/roc_curve.py ../files/hmms/u1_binding_tgf/u1_2_8.tgf ../files/sequences/context_real_donors.raw > "$ROC_DATA/u1_2_8_roc.tsv"
../scripts/roc_curve.py ../files/hmms/u1_binding_tgf/u1_3_7.tgf ../files/sequences/context_real_donors.raw > "$ROC_DATA/u1_3_7_roc.tsv"
